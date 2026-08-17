def person_listener(f):
    def wrapper(people):
        return [f(person) for person in people]
    return wrapper


@person_listener
def name_format(person):
    return ("Sr. " if person[3] == "H" else "Sra. ") + person[0] + " " + person[1]


if __name__ == '__main__':    
    people = [input(f"{i+1}: ").split() for i in range(int(input("Total personas: ")))]
    print(*name_format(people), sep="\n")
