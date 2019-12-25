import os

stage = os.getenv('STAGE', 'DEV').upper()

output = "We are running in " + stage

if stage.startswith('PROD'):
    output = "DANGER!!! - " + output

print(output)
