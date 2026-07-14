// Last updated: 7/14/2026, 10:11:52 AM
import java.util.*;
class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        int i = 0;
        while (i < words.length) {
            int lineLength = words[i].length();
            int j = i + 1;
            while (j < words.length &&
                   lineLength + 1 + words[j].length() <= maxWidth) {
                lineLength += 1 + words[j].length();
                j++;
            }
            int gaps = j - i - 1;
            StringBuilder line = new StringBuilder();
            if (j == words.length || gaps == 0) {
                for (int k = i; k < j; k++) {
                    line.append(words[k]);
                    if (k < j - 1) {
                        line.append(" ");
                    }
                }
                while (line.length() < maxWidth) {
                    line.append(" ");
                }
            } else {
                int totalChars = 0;
                for (int k = i; k < j; k++) {
                    totalChars += words[k].length();
                }
                int totalSpaces = maxWidth - totalChars;
                int spacesPerGap = totalSpaces / gaps;
                int extraSpaces = totalSpaces % gaps;
                for (int k = i; k < j - 1; k++) {
                    line.append(words[k]);
                    for (int s = 0; s < spacesPerGap; s++) {
                        line.append(" ");
                    }
                    if (extraSpaces > 0) {
                        line.append(" ");
                        extraSpaces--;
                    }
                }
                line.append(words[j - 1]);
            }
            result.add(line.toString());
            i = j;
        }
        return result;
    }
}