class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0])); // sort by start

        List<int[]> merged = new ArrayList<>();

        int [] curr = intervals[0];

        for (int i = 1; i < intervals.length; i++) {
            int[] interval = intervals[i];
            if (curr[1] >= interval[0]) {
                curr[1] = (curr[1] > interval[1] ? curr[1] : interval[1]);
            }
            else {
                merged.add(curr);
                curr = interval;
            }
        }
        merged.add(curr);

        return merged.toArray(new int[merged.size()][]);
    }
}
