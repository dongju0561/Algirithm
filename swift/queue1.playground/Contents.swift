class Queue<T>{
    var queue: [T] = []
    
    var isEmpty: Bool{
        
        return queue.isEmpty
    }
    var count: Int{
        return queue.count
    }
    
    func dequeue() -> T?{
        return queue.isEmpty ? nil : queue.removeLast()
    }
    
    func enqueue(_ element: T){
        queue.append(element)
    }
}

var q1 = Queue<Int>()

print(q1.count)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())

