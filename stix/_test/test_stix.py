

from stix import Bundle

def main():

    bundle = Bundle(spec_version='2.0')

    print bundle.to_dict()



if __name__ == '__main__':
    main()

# EOF
