package com.guidance;

public class AptitudeClassifier {
    public static int classify(double[] scores) {
        double avg = 0.0;
        for (double score : scores) {
            avg += score;
        }
        avg /= scores.length;
        return avg > 75 ? 3 : (avg > 50 ? 2 : 1);
    }
}