class Q1{
    public static void main(String[] args){
        int[] arr1 = {34, 7, 23, 32, 5, 62};
        int[] arr2 = {14, 55, 3, 27, 18, 41};

        mergeSort(arr1, 0, arr1.length - 1);
        mergeSort(arr2, 0, arr2.length - 1);

    }

    public static void mergeSort(int[] arr, int left, int right){
        if (left < right){
            int mid = (left + right) / 2;

            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);

            merge(arr, left, mid, right);
        }
    }

    public static void merge(int[] arr, int left, int mid, int right){
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] L = new int[n1];
        int[] R = new int[n2];

        for(int i = 0; i < n1; i++){
            L[i] = arr[left + i];
        }

        for(int j = 0; j < n2; j++){
            R[j] = arr[mid + 1 + j];
        }

    }
}