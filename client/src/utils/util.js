/*
    FUNCTION: RANGE

    INPUT:
        size: integer
        startAt: integer

    DESCRIPTION: gets a range of numbers starting from 
*/
export function range(start, end) {
    if (start >= end) return [0];
    return [...Array(end - start).keys()].map(i => i + start);
}