import string 

a = string.ascii_lowercase
b = string.ascii_uppercase

for x in a:
    s = f"""
    if event.key == pygame.K_{x}:
        self.ifValidInput(blue_rect.y, blue_rect.x, '{x.upper()}')
    """
    print(s)