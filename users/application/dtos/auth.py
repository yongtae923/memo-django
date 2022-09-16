

from rest_framework import serializers

class PhoneNumberRequestDTO(serializers.Serializer):
    """
    public class PhoneNumberRequestModel
    {
        [Required]
        [DataType(DataType.PhoneNumber)]
        public string Phone { get; set; }
    }
    """
    phone = serializers.CharField()

class VerifyCodeDTO(serializers.Serializer):
    code = serializers.CharField()
    phone = serializers.CharField()