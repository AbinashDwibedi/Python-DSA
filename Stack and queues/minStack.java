// import java.util.Stack;
// class MinStack {
    
//     Stack<int []> st;

//     public MinStack() {
//         this.st = new Stack<>();
//     }
    
//     public void push(int val) {
//         if (st.empty()){
//             this.st.push(new int[]{val,val});
//         }
//         else{
//             int minVal = Math.min(val,st.peek()[1]);
//             this.st.push(new int[]{val,minVal});
//         }
//     }
    
//     public void pop() {
//         this.st.pop();
//     }
    
//     public int top() {
//         return this.st.peek()[0];
//     }
    
//     public int getMin() {
//         return this.st.peek()[1];
//     }
// }

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */

import java.util.Stack;
class MinStack {
    
    Stack<Long> st;
    long minVal;

    public MinStack() {
        this.st = new Stack<>();
    }
    
    public void push(int val) {
        if (st.isEmpty()){
            this.st.push((long)val);
            this.minVal = (long)val;
        }
        else{
            if (val >= this.minVal){
                this.st.push((long)val);
            }
            else{
                long tmp = (2L*val) - this.minVal;
                this.st.push(tmp);
                this.minVal = (long)val;
            }
        }
    }
    
    public void pop() {
        if (this.minVal > this.st.peek()){
            long tmp = (2L * this.minVal ) - this.st.pop();
            this.minVal = tmp;
        }
        else{
            this.st.pop();
        }
    }
    
    public int top() {
        if (this.minVal > this.st.peek()){
            return (int)this.minVal;
        }
        return (int)(long)this.st.peek();
    }
    
    public int getMin() {
        return (int)this.minVal;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */