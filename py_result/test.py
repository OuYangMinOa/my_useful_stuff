from rs_type import Result, Err, Ok

def devide(a: int, b: int) -> Result[int, str]:
    if b == 0:
        return Err("Division by zero error")
    return Ok(a // b)

def main() -> None:
    result : Result[int, str] = devide(10, 0)
    match result:
        case Ok():
            print(f"Result: {result.value}")
        case Err():
            print(f"Error: {result.error}")
            
    result : Result[int, str] = devide(10, 2)
    match result:
        case Ok():
            print(f"Result: {result.value}")
        case Err():
            print(f"Error: {result.value}")


        
if __name__ == "__main__":
    main()