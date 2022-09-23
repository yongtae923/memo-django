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
    context_key = serializers.CharField()


class RegisterDTO(serializers.Serializer):
    """
    [DataType(DataType.EmailAddress)]
    public string Email { get; set; }
    [Required]
    public string Password { get; set; }
    [Required]
    public string Name { get; set; }
    [Required]
    public string Nickname { get; set; }
    [Required]
    [DataType(DataType.PhoneNumber)]
    public string Phone { get; set; }
    """

    email = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    nickname = serializers.CharField()
    phone = serializers.CharField()
    context_key = serializers.CharField()


class LoginDTO(serializers.Serializer):
    id = serializers.CharField()
    password = serializers.CharField()
