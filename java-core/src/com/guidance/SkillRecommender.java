package com.guidance;

import java.util.ArrayList;
import java.util.List;

public class SkillRecommender {
    public static List<String> recommendCareers(List<String> skills) {
        List<String> careers = new ArrayList<>();
        for (String skill : skills) {
            skill = skill.trim().toLowerCase();
            switch (skill) {
                case "biology":
                    careers.add("Doctor");
                    break;
                case "math":
                    careers.add("Engineer");
                    break;
                case "debate":
                    careers.add("Lawyer");
                    break;
                case "writing":
                    careers.add("Journalist");
                    break;
                case "finance":
                    careers.add("Chartered Accountant");
                    break;
                default:
                    careers.add("Generalist");
            }
        }
        return careers;
    }
}