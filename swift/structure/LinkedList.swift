class Node<T>{
    var item: T?
    var next: Node?

    init(_ item: T,_ next: Node? = nil){
        self.item = item
        self.next = next
    }
}

class LinkedList<T>{
    private var head: Node<T>?

    init(head: Node<T>? = nil){}

    //연결리스트의 맨 마지막에 노드를 추가해주는 함수
    func append(item: T?) {
        //head가 어떤 노드도 가리키고 있지 않을 경우
        if head == nil{
            //그냥 head에 새롭게 추가된 노드를 가리키게 하는 코드
            if let item = item{
                head = Node(item)
            }
            return
        }
        //다음 노드로 반복 이동하면서 맨 끝의 노드로 이동하는 코드
        var node = head
        while(node?.next != nil){
            node = node?.next
        }

        //맨 마지막 노드에 도착하고 새로운 노드를 추가
        guard let item = item else {
            return
        }
        node?.next = Node(item)
    }

    func insert(item: T, at index: Int){
        //head가 어떤 노드도 가리키고 있지 않을때
        if(head == nil){
            //추가된 노드를 head가 가리키게 하고 반환
            head = Node(item)
            return
        }
        //A -> B -> C
        //맨 마지막 노드를 찾기위한 코드
        var node = head
        for _ in 0..<(index - 1){
            //현재 노드의 다음 노드가 nil인 경우 즉 현재 노드가 마지막 노드인 경우 반복문을 탈출
            if node?.next == nil{ break }
            node = node?.next
        }

        //앞선 노드의 다음 노드를 임시변수인 nextNode에 할당
        let nextNode = node?.next

        //새롭게 추가된 노드를 앞선 노드 뒤에 추가하는 코드
        node?.next = Node(item)

        //추가된 노드의 next를 기존의 앞선 노드의 다음 노드와 연결해주는 코드
        node?.next?.next = nextNode
    }

    func printLinkedList(){
        guard let head = head else{
            print("리스트가 비어있습니다.")
            return
        }
        print(head)
        print(Int(head.item))
        var node = head
        repeat {

            print("\(node.item) -> ", terminator: "")
            node = node.next!
        } while (node.next != nil)  
        print("nil")

    }
}


//노드 생성
var nodeA = Node(1)
var nodeB = Node(3)
var nodeC = Node(11)

var linkedList = LinkedList<Node<Int>>()

linkedList.append(item: nodeA)
linkedList.append(item: nodeB)
linkedList.append(item: nodeC)

linkedList.printLinkedList()