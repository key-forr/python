from calculator import square

def main():
        test_square()      


def test_square():
    try:
        assert square(2) == 4, "square(2) should be 4"
    except AssertionError as e:
        print(e) 
        
    try: 
        assert square(3) == 9, "square(3) should be 9"
    except AssertionError as e:
        print(e)  

    try:
        assert square(-3) == 9, "square(-3) should be 9"
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()