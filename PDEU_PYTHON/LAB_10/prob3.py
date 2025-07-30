name = input("Enter name: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")

with open('contact.vcf', 'w') as f:
    f.write("BEGIN:VCARD\n")
    f.write("VERSION:3.0\n")
    f.write(f"N:{name};;;\n")
    f.write(f"TEL:{phone}\n")
    f.write(f"EMAIL:{email}\n")
    f.write("END:VCARD\n")
