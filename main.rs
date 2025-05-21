#[derive(Debug, Clone)]
struct Node {
    data: i32,
    next: Option<Box<Node>>,
}

#[derive(Debug, Clone)]
struct Stack {
    head: Option<Box<Node>>,
    size: u32,
}

impl Stack {
    pub fn new() -> Self {
        Stack {
            head: None,
            size: 0,
        }
    }

    pub fn insert(&mut self, data: i32) {
        let new_node = Box::new(Node {
            data,
            next: self.head.take(), 
        });
        self.head = Some(new_node);
        self.size += 1;
    }

    pub fn lowest_value(&self) {
        if self.head.is_none() {
            println!("Stack is empty.");
            return;
        }
    
        let mut current = self.head.as_deref();
        let mut low = current.unwrap().data;
    
        while let Some(node) = current {
            if node.data < low {
                low = node.data;
            }
            current = node.next.as_deref();
        }
    
        println!("The lowest value of the Stack is: {}", low);
    }
    

    fn print(&self) {
        let mut current = self.head.as_ref();
        while let Some(node) = current {
            print!("{} -> ", node.data);
            current = node.next.as_ref();
        }
        println!("None");
    }    
}

fn main() {
    let mut stack = Stack::new();
    stack.insert(0);
    stack.insert(1);
    stack.insert(2);
    stack.insert(-1);
    stack.lowest_value();
    stack.insert(2);
    stack.print()
}
