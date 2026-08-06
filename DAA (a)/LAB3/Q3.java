public class Q3 {
    public static void main(String[] args){
        int arr[] = {2, 3, 5, 6, 7, 9, 12, 14, 15, 17, 14, 12, 20};
        int n = arr.length;
        for (int i = 0; i < arr.length - 1; i++){
            for (int j = 0; j < arr.length - i - 1; j++){
                if (arr[j] > arr[j + 1]){
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
        for (int j = 0; j < arr.length; j++){
            System.out.print(arr[j] + " ");
        }
        System.out.println();

        int low = arr[0];
        int high = arr[n - 1];
        int key = 7;
        boolean found = false;
        while (low <= high) {
            int mid = (low + high) / 2;

            if (arr[mid] == key) {
                System.out.println("Element " + key + " found at index " + mid);
                found = true;
                break;
            } else if (arr[mid] < key) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        if (!found) {
            System.out.println("Element " + key + " not found in the array.");
        }
    }
}