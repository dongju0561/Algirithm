struct Queue <T>{
    private var queue: [T] = []
    public var count: Int{
        return queue.count
    }
    public var isEmpty: Bool{
        return queue.isEmpty
    }
    public mutating func enqueue(_ element: T){
        queue.append(element)
    }
    public mutating func denqueue() -> T?{
        return isEmpty ? nil : queue.removeFirst()
        //제일 처음에 들어간 요소부터 꺼내오기
    }
}

var queue = Queue<Int>()

print(queue.count)//만약 배열에 요소가 아무것도 없다면 출력하지 않는다.
print(queue.isEmpty)

queue.enqueue(1)
print(queue.count)
queue.enqueue(2)
queue.enqueue(3)

print(queue.count)
print(queue.isEmpty)

print(queue.denqueue()!)
print(queue.denqueue()!)
print(queue.denqueue()!)
