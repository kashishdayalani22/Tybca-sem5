public class Q1 {
    
    static void heapify (int arr[], int n, int i){
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if(left<n && arr[left] > arr[largest]){
            largest = left;
        }

        if (right < n && arr[right] > arr[largest]) {
            largest = right;
        }

        if(largest !=i){
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;

            heapify(arr,n,largest);
        }
    }
    static void heapsort(int arr[]){
        
        int n = arr.length;

        for(int i = n / 2 - 1; i >= 0 ;i--){
            heapify(arr,n,i);
        }

        for(int i=n-1; i>0; i--){
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            heapify(arr,i,0);
        }
    }
    static void printArray(int arr[]) {
        for(int num:arr){
            System.out.print(num + " ");
        }
        System.out.println();
        
    }
    
    
    
    
    
    
    public static void main(String[] args) {
        int arr[] = { 55,20,3,66,77,44,22};

        System.out.println("original");
        printArray(arr);

        heapsort(arr);

        System.out.println("SORTED");
        printArray(arr);

    }
    
}
