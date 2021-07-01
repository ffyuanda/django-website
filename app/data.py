class Contact:
    def __init__(self) -> None:
        self.name = "Shaoxuan Yuan"
        self.email = "shaoxuan.yuan02@gmail.com"
        self.address = "Guangzhou, China"
        self.github = "https://github.com/ffyuanda"
    
    def __str__(self) -> str:
        info = ""
        for key, item in self.__dict__.items():
            info += f"{key}: {item}\n"

        return info.strip()
