package com.guidance;

import java.util.ArrayList;
import java.util.List;

public class RecommendationEngine {
    public static List<String> getRecommendations(int aptitude, List<String> skillCareers) {
        List<String> finalRecs = new ArrayList<>(skillCareers);
        if (aptitude == 3) finalRecs.add("Research Roles");
        if (aptitude == 2) finalRecs.add("Mid-level Technical Jobs");
        if (aptitude == 1) finalRecs.add("Skill Development Programs");
        return finalRecs;
    }
}