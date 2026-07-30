public class  Q1 {
    public static void main(String[] args) {
        int[] arr = {55,20,3,66,77};
        for(int i=0; i<arr.length -1; i++){
            for(int j=0; j<arr.length -1; j++){

                if(arr[j] > arr[j +1]){
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
        for(int j=0; j < arr.length; j++){
            System.out.print(arr[j] + " , ");
        }
    }
}
