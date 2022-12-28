struct Stack <T>{
    private var stack: [T] = []
    
    public var count: Int{
        return stack.count
    }
    public var isEmpty: Bool{
        return stack.isEmpty
    }
    public mutating func pop() -> T?{
        return isEmpty ? nil : stack.popLast()
    }
    public mutating func push(_ element: T){
        stack.append(element)
        //제일 마지막에 들어간 요소 먼저 꺼내옴
    }
}

var stack = Stack<Int>()

stack.count
stack.isEmpty
stack.push(1)
stack.push(2)
stack.push(3)

stack.count
stack.isEmpty

print(stack.pop()!)
print(stack.pop()!)
print(stack.pop()!)

