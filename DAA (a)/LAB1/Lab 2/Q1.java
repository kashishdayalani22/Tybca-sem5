public class Q1{
    public static void main(String[] args){
        int[] arr = {55, 20, 3, 66, 77};
        int n = arr.length;
        for (int i = 0; i < n - 1; i++){
            for (int j = 0; j < n - i - 1; j++){
                if (arr[j + 1] > arr[j]){
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
        for (int x = 0; x < arr.length; x++){
            System.out.print(arr[x] + " ");
        }
    }
}