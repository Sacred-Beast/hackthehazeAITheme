package com.guidance;

import java.util.ArrayList;
import java.util.List;

public class GoalExtractor {
    public static List<String> extractGoals(String input) {
        List<String> goals = new ArrayList<>();
        input = input.toLowerCase();
        if (input.contains("doctor")) goals.add("Medical");
        if (input.contains("engineer")) goals.add("Engineering");
        if (input.contains("civil")) goals.add("UPSC");
        if (input.contains("startup")) goals.add("Entrepreneurship");
        return goals;
    }
}