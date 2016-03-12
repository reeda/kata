package com.github.reeda.kata;

import com.google.common.collect.Lists;
import java.util.List;

public class PrimeFactors {
    public static List<Integer> generate(int n) {
        List<Integer> factors = Lists.newArrayList();
        for (int candidate = 2; n > 1; candidate++) {
            for (; n % candidate == 0; n /= candidate) {
                factors.add(candidate);
            }
        }
	    return factors;
    }
}
