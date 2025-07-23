from string.templatelib import Template, Interpolation

username = "user123"
password = "123!"
def masking(template: Template) -> str:
    """Mask the values"""
    parts: list[str] = []
    mask_char= '*'
    part=''
    for item in template:
        if isinstance(item, Interpolation):
            mask_char=mask_char * len(item.value)
            part=mask_char
        else:
            part=item
        parts.append(part)
    return "".join(parts)



masked_interpolations = masking(t"User {username} logged in with password {password}")
print(masked_interpolations)                              
