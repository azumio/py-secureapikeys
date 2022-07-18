from google.cloud import kms
import crcmod
import six
import base64


class SecureApiKeys:
    """
    This class decrypts and caches the Azumio Api Keys
    """

    def __init__(self, project_id, location_id, key_ring_id, key_id):
        self.project_id = project_id
        self.location_id = location_id
        self.key_ring_id = key_ring_id
        self.key_id = key_id
        self.client = kms.KeyManagementServiceClient()
        self.key_name = self.client.crypto_key_path(project_id, location_id,
                                                    key_ring_id, key_id)
        self.cache = {}

    def decrypt_key(self, encrypted_key):
        """
        Decrypts the key using the Google Cloud KMS service
        """

        if encrypted_key in self.cache:
            return self.cache[encrypted_key]

        ciphertext = base64.b64decode(encrypted_key)
        ciphertext_crc32c = SecureApiKeys.crc32c(ciphertext)
        # Call the API.
        decrypt_response = self.client.decrypt(
            request={
                'name': self.key_name,
                'ciphertext': ciphertext,
                'ciphertext_crc32c': ciphertext_crc32c
            })
        # https://cloud.google.com/kms/docs/data-integrity-guidelines
        if not decrypt_response.plaintext_crc32c == SecureApiKeys.crc32c(
                decrypt_response.plaintext):
            raise Exception(
                'The response received from the server was corrupted in-transit.'
            )
        api_key = decrypt_response.plaintext.decode("utf-8")
        self.cache[encrypted_key] = api_key
        return api_key

    @staticmethod
    def crc32c(data):
        """
        Calculates the CRC32C checksum of the provided data.
        Args:
            data: the bytes over which the checksum should be calculated.
        Returns:
            An int representing the CRC32C checksum of the provided bytes.
        """
        crc32c_fun = crcmod.predefined.mkPredefinedCrcFun('crc-32c')
        return crc32c_fun(six.ensure_binary(data))
