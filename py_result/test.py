from rs_type import Result, Err, Ok

def devide(a: int, b: int) -> Result[int, str]:
    if b == 0:
        return Err("Division by zero error")
    return Ok(a // b)

def main() -> None:
    result = devide(10, 0)
    if result.is_ok():
        print(f"Result: {result.unwrap()}")
    else:
        print(f"Error: {result.unwrap_err()}")
    
    result = (devide(10, 2).
                map(lambda x: x * 2).
                map_err(lambda x: f"Error: {x}").
                and_then(lambda x: x + 1).
                unwrap()
            )
    print(result)
    
    

if __name__ == "__main__":
    main()