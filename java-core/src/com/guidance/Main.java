package com.guidance;

import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("🎯 Welcome to the Career Guidance CLI Tool");

        System.out.print("Enter aptitude scores (comma-separated): ");
        String[] scoreStrings = scanner.nextLine().split(",");
        double[] scores = Arrays.stream(scoreStrings).mapToDouble(Double::parseDouble).toArray();

        int aptClass = AptitudeClassifier.classify(scores);
        System.out.println("🧠 Predicted Aptitude Class: " + aptClass);

        System.out.print("Enter your goal statement: ");
        String goal = scanner.nextLine();
        List<String> goals = GoalExtractor.extractGoals(goal);
        System.out.println("🎯 Extracted Goals: " + goals);

        System.out.print("Enter your current skills (comma-separated): ");
        String[] skillInputs = scanner.nextLine().split(",");
        List<String> skills = Arrays.asList(skillInputs);

        List<String> careers = SkillRecommender.recommendCareers(skills);
        System.out.println("🧩 Career Matches: " + careers);

        List<String> finalRecs = RecommendationEngine.getRecommendations(aptClass, careers);
        System.out.println("🔁 Final Career Recommendations: " + finalRecs);

        scanner.close();
    }
}