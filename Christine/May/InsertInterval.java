class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> inserted = new ArrayList<>();

        int i = 0;

        while ((i < intervals.length) && (intervals[i][1] < newInterval[0])) {
            inserted.add(intervals[i]);

            i++;
        }

        int first = newInterval[0];
        int second = newInterval[1];

        while ((i < intervals.length) && (intervals[i][0] <= second)) {
            first = (first < intervals[i][0] ? first : intervals[i][0]);
            second = (second > intervals[i][1] ? second : intervals[i][1]);

            i++;
        }

        inserted.add(new int[]{first, second});

        while (i < intervals.length) {
            inserted.add(intervals[i]);

            i++;
        }
        
        return inserted.toArray(new int[inserted.size()][]);
    }
}
