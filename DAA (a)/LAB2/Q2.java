public class Q2 {
    public static void main(String[] args){
        int[] arr = {3, 2, 0, 5, 3, 7, 9, 1, 1, 3};
        int[] count_arr = new int[10];
        int[] sorted_arr = new int[arr.length];

        for (int i = 0; i < count_arr.length; i++){
            count_arr[arr[i]] = count_arr[arr[i]] + 1;
        }

        for (int j = 0; j < count_arr.length - 1; j++){
            count_arr[j + 1] = count_arr[j] + count_arr[j + 1];
        }

        for (int x = 0; x < count_arr.length; x++){
            sorted_arr[count_arr[arr[x]] - 1] = arr[x];
            count_arr[arr[x]] = count_arr[arr[x]] - 1;
        }  

        for (int x = 0; x < arr.length; x++){
            System.out.print(sorted_arr[x] + " ");
        }
    }
}