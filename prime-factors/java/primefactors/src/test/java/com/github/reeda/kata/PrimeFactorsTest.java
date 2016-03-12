package com.github.reeda.kata;

import org.junit.Test;
import org.junit.Assert;

public class PrimeFactorsTest {

    @Test
    public void testOne() {
	Assert.assertEquals(Lists.newArrayList(), PrimeFactors.generate(1));
    }
}
