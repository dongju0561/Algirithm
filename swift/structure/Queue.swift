class Queue<T>{
    private var queue: [T] = [] 
    public var isEmpty: Bool{
        return queue.isEmpty
    }
    public var count: Int{
        return queue.count
    }
    public func enqueue(_ element: T){
        queue.append(element)
    }
    public func dequeue() -> T?{
        return queue.isEmpty ? nil : queue.removeFirst()
    }
}

var q1 = Queue<Int>()

q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())