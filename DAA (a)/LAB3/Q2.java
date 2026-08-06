class Q2{
    public static void main(String[] args){
        int[] arr1 = {1, 3, 5};
        int[] arr2 = {2, 4, 6, 8, 10};
        int[] arr_sorted = new int[arr1.length + arr2.length];
        
        int i = 0;
        int j = 0;
        int k = 0;

        while (i < arr1.length && j < arr2.length){
            if(arr1[i] < arr2[j]){
                arr_sorted[k] = arr1[i];
                k++;
                i++;
            } else {
                arr_sorted[k] = arr2[j];
                k++;
                j++;
            }
        }
        while(i < arr1.length){
            arr_sorted[k++] = arr1[i++];
        }

        while (j < arr2.length){
            arr_sorted[k++] = arr2[j++];
        }

        System.out.print("Merged Sorted List: ");
        for (int x = 0; x < arr_sorted.length; x++) {
            System.out.print(arr_sorted[x] + " ");
        }
    }
}