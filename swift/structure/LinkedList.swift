class Node<T>{
    var item: T?
    var next: Node?

    init(_ item: T,_ next: Node? = nil){
        self.item = item
        self.next = next
    }
}


