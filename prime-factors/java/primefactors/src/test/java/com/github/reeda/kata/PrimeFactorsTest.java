package com.github.reeda.kata;

import com.google.common.collect.Lists;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PrimeFactorsTest {

    @Test
    public void testOne() {
	    assertEquals(Lists.newArrayList(), PrimeFactors.generate(1));
    }

    @Test
    public void testTwo() {
        assertEquals(Lists.newArrayList(2), PrimeFactors.generate(2));
    }

    @Test
    public void testThree() {
        assertEquals(Lists.newArrayList(3), PrimeFactors.generate(3));
    }

    @Test
    public void testFour() {
        assertEquals(Lists.newArrayList(2, 2), PrimeFactors.generate(4));
    }

    @Test
    public void testSix() {
        assertEquals(Lists.newArrayList(2, 3), PrimeFactors.generate(6));
    }

    @Test
    public void testEight() {
        assertEquals(Lists.newArrayList(2, 2, 2), PrimeFactors.generate(8));
    }

    @Test
    public void testNine() {
        assertEquals(Lists.newArrayList(3, 3), PrimeFactors.generate(9));
    }
}
