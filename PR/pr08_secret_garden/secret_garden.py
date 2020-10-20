"""Secret Garden."""
import base64


class Decoder:
    """Decoder class."""

    def __init__(self, file: str, key: str):
        """
        Decoder constructor.

        :param file: Input file
        :param key: Very secret key
        """
        self.file = file
        self.key = key

    def read_code_from_file(self) -> list:
        """
        Read file lines to a list.

        File comes from class constructor.

        :return: List of file lines
        """
        lines = []
        with open(self.file, encoding='utf-8') as file:
            for line in file:
                lines.append(line.strip())
        return lines

    @staticmethod
    def decode_from_base64(data: str) -> str:
        """
        Decode base64 string to utf-8 string.

        :param data: Base64 format string
        :return: Utf-8 format string
        """

        a = base64.b64decode(data)
        return a.decode("utf-8")

    def calculate_cipher_step(self) -> int:
        """
        Calculate cipher step.

        Cipher key comes from constructor.
        Formula is sum of UNICODE value of each letter.
        Example: "Hi" -> 72 + 105 -> 177

        :return: Cipher step as integer
        """
        sum = 0
        for char in self.key:
            sum += ord(char)
        return sum

    def decode(self) -> list:
        """
        Decode file with key.

        For correct answer you have to convert file lines from base64 to utf-8.

        To decode one line you have to take a UNICODE value of a letter, subtract cipher step and take mod of 255.
        After that you have to convert that number back to a character.
        Example: key = 'test', decoded_data = "+%'"
        '+' -> (43 - 448) % 255 -> 'i' -> ... -> 'ice'

        :return: List of decoded lines
        """
        step = self.calculate_cipher_step()
        lines = self.read_code_from_file()
        decode = []
        for line in lines:
            utf8 = self.decode_from_base64(line)
            word = ""
            for char in utf8:
                char = chr((ord(char) - step) % 255)
                word += char
            decode.append(word)
        return decode


class SecretGarden:
    """SecretGarden class."""

    def __init__(self, file: str, key: str):
        """
        SecretGarden constructor.

        :param file: Input file
        :param key: Very secret key
        """
        self.file = file
        self.key = key

    def decode_messages(self) -> list:
        """
        Use Decoder class to decode messages.

        :return: List of decoded lines
        """
        decoder = Decoder(self.file, self.key)
        return decoder.decode()

    def find_secret_locations(self) -> list:
        """
        Find all secret locations.

        You have to use decoded messages here. These messages contain a starting coordinate on first line e.g. '1;4'.
        First number shows position on east-west scale and second number shows position on north-south scale.
        Second line is empty.
        Third line contains steps to reach to the secret location e.g. 'NEEWSS'.
        Possible steps are 'N' (north), 'E' (east), 'S' (south) and 'W' (west). Each step moves your position by 1.

        :return: List of tuples with secret location coordinates
        """
        routes = self.decode_messages()
        locations = []
        for route in routes:
            route = route.split("\n\n")
            point = route[0].split(";")
            point = list(map(int, point))
            for step in route[1]:
                if step == "N":
                    point[1] += 1
                elif step == "E":
                    point[0] += 1
                elif step == "S":
                    point[1] += -1
                elif step == "W":
                    point[0] += -1
            point = tuple(point)
            locations.append(point)
        return locations


if __name__ == '__main__':
    d = Decoder('pr08_example_data.txt', 'Fat Chocobo')
    print(d.read_code_from_file())  # ['KS0uNyktBgZBT08=', ...]
    print(d.decode_from_base64('MDsyCgpOTlNXV0U='))  # 0;2\n\nNNSWWE
    print(d.calculate_cipher_step())  # 70 + 97 + 116 + 32 + ... -> 1016
    print(d.decode())  # ['-12;-1\n\nESS', ...]

    sg = SecretGarden('pr08_example_data.txt', 'Fat Chocobo')
    print(sg.decode_messages())  # ['-12;-1\n\nESS', ...]
    print(sg.find_secret_locations())  # [(-11, -3), (20, -13), (1, -3), (-2, -5), (10, 4), (6, -13), (2, -6)]
