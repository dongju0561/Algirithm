class Stack<T>{
    private var stack: [T] = []

    public var count: Int{
        return stack.count
    }
    public var isEmpty: Bool{
        return stack.isEmpty
    }
    public func push(_ element: T){
        return stack.append(element)
    }
    public func pop() -> T?{
        return stack.isEmpty ? nil : stack.removeLast()
    }
}

var s1 = Stack<Int>()

s1.push(1)
s1.push(2)
s1.push(3)

print(s1.pop())
print(s1.pop())
print(s1.pop())
