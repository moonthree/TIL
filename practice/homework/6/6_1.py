def ssn(ssn):
    return ssn[:6] + '*'*len(ssn[6:])


if __name__ == "__main__":
    print(ssn('960725-111111'))