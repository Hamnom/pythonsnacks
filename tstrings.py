from string import Template

template = Template("$country has $count states.")
output = template.substitute(country="United States", count=50)

print(output)