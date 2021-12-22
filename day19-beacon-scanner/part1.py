#!python3

from math import sqrt
from decimal import *
from sys import exit

# with open('input.txt') as file:
with open('example.txt') as file:
    scanner_input = [
        [
            [
                int(coord)
                for coord in beacon.split(',')
            ]
            for beacon in scanner.split('\n')[1:]
        ]
        for scanner in file.read().split('\n\n')
    ]

num_scanners = len(scanner_input)
scanners = {
    # Which scanner
    0: {
        # Which axis corresponds to which coordinate, in order
        'idx': {
            'x': 0,
            'y': 1,
            'z': 2
        },
        # How polarized is the axis (1/-1)
        'sgn': {
            'x': 1,
            'y': 1,
            'z': 1
        },
        'pos': {
            'x': 0,
            'y': 0,
            'z': 0
        }
    }
}
pairs = {}
beacons = {}

for s in range(0, num_scanners):
    scanner = scanner_input[s]
    for i in range(0, len(scanner) - 1):
        for j in range(i + 1, len(scanner)):
            one, two = scanner[i], scanner[j]
            x1, y1, z1 = one
            x2, y2, z2 = two
            # distance = sqrt(sum([ pow(x1 - x2, 2), pow(y1 - y2, 2), pow(z1 - z2, 2) ]))
            distance = sum([ pow(x1 - x2, 2), pow(y1 - y2, 2), pow(z1 - z2, 2) ])
            if not distance in pairs:
                pairs[distance] = {}
            pairs[distance][s] = (one, two)

undetermined_scanners = list(set(range(1, num_scanners)))
determined_scanners = { 0 }
skipped = set()
while undetermined_scanners:
    scanner_id = undetermined_scanners.pop(0)
    ref_id = None

    # Find reference scanner that overlaps
    common_pairs = {}
    for ref_scanner in determined_scanners:
        # Find a ref scanner with the best coverage
        common_pairs_candidate = dict([ (key, value) for key, value in pairs.items() if ref_scanner in value and scanner_id in value ])
        # Determine, if at least 12 beacons
        distinct_beacons = []
        for pair in common_pairs_candidate.values():
            beacon_start, beacon_end = pair[ref_scanner]
            if beacon_start not in distinct_beacons:
                distinct_beacons.append(beacon_start)
            if beacon_end not in distinct_beacons:
                distinct_beacons.append(beacon_end)
        if len(distinct_beacons) < 12:
            continue
        ref_id = ref_scanner
        common_pairs = common_pairs_candidate
        break
    if not common_pairs:
        if scanner_id in skipped:
            # Trigger failsafe. Skip
            print(f'Discarding scanner {scanner_id}.')
            continue
        undetermined_scanners.append(scanner_id)
        skipped.add(scanner_id)
        continue

    # Pairs with a common point
    pair_first = None
    pair_second = None
    # Same point, two perspectives
    start_a = None
    start_b = None
    for key_first in common_pairs:
        pair_first = common_pairs[key_first]
        points = pair_first[ref_id]  # Nullth scanner, first pair
        # Avoid point pairs, which do not differ in all dimensions
        print(f'{points}')
        if points[0][0] == points[1][0] or points[0][1] == points[1][1] or points[0][2] == points[1][2]:
            continue
        other_keys = list(common_pairs.keys())
        other_keys.remove(key_first)
        for key_other in other_keys:
            pair_other = common_pairs[key_other]
            p1, p2 = pair_other[ref_id]  # Nullth scanner, second pair
            if p1[0] == p2[0] or p1[1] == p2[1] or p1[2] == p2[2]:
                continue
            if p1 in points:
                start_a = p1
                pair_second = pair_other
                break
            if p2 in points:
                start_a = p2
                pair_second = pair_other
                break
        if pair_second:
            break

    # Find the point from the other perspective
    start_b = [
        p for p in pair_second[scanner_id]
        if p in pair_first[scanner_id]
    ]
    start_b = start_b[0]

    # Find the other point, both perspectives
    points_a = list(pair_first[ref_id])  # Nullth scanner
    points_a.remove(start_a)
    end_a = points_a[0]
    points_b = list(pair_first[scanner_id])
    points_b.remove(start_b)
    end_b = points_b[0]

    # Determine scanner characteristics
    new_scanner = {
        'idx': {},
        'sgn': {},
        'pos': {}
    }
    ref_scanner = scanners[ref_id]  # Nullth scanner
    ref_ix = ref_scanner['idx']['x']
    ref_iy = ref_scanner['idx']['y']
    ref_iz = ref_scanner['idx']['z']
    ref_px = ref_scanner['pos']['x']
    ref_py = ref_scanner['pos']['y']
    ref_pz = ref_scanner['pos']['z']
    ref_sx = ref_scanner['sgn']['x']
    ref_sy = ref_scanner['sgn']['y']
    ref_sz = ref_scanner['sgn']['z']
    ref_dx = (end_a[ref_ix] - start_a[ref_ix]) * ref_sx
    ref_dy = (end_a[ref_iy] - start_a[ref_iy]) * ref_sy
    ref_dz = (end_a[ref_iz] - start_a[ref_iz]) * ref_sz
    mismatch = False
    if ref_dx == ref_dy or ref_dx == ref_dz or ref_dy == ref_dz:
        mismatch = True
    for i in range(0, 3):
        if mismatch:
            break
        start = start_b[i]
        end = end_b[i]
        d = end - start
        if abs(d) == abs(ref_dx) and not new_scanner['idx'].get('x'):
            print('x')
            new_scanner['idx']['x'] = i
            new_scanner['sgn']['x'] = int(d / ref_dx)
            new_scanner['pos']['x'] = start_a[ref_ix] * ref_sx - ref_px - start * new_scanner['sgn']['x']
        elif abs(d) == abs(ref_dy) and not new_scanner['idx'].get('y'):
            print('y')
            new_scanner['idx']['y'] = i
            new_scanner['sgn']['y'] = int(d / ref_dy)
            new_scanner['pos']['y'] = start_a[ref_iy] * ref_sy - ref_py - start * new_scanner['sgn']['y']
        elif abs(d) == abs(ref_dz) and not new_scanner['idx'].get('z'):
            print('z')
            new_scanner['idx']['z'] = i
            new_scanner['sgn']['z'] = int(d / ref_dz)
            new_scanner['pos']['z'] = start_a[ref_iz] * ref_sz - ref_pz - start * new_scanner['sgn']['z']
        else:
            # Rare situation, where the range is valid, but pair is different
            mismatch = True
    if mismatch:
        undetermined_scanners.insert(0, scanner_id)
        determined_scanners.remove(ref_id)
        continue

    scanners[scanner_id] = new_scanner
    determined_scanners = set(scanners)
    skipped = set()  # Reset loop failsafe
    print(new_scanner)

points_normalized = []

for scanner_id, props in scanners.items():
    point_pairs = [ value[scanner_id] for value in pairs.values() if scanner_id in value ]
    for pair in point_pairs:
        for point in pair:
            x = props['pos']['x'] + point[props['idx']['x']] * props['sgn']['x']
            y = props['pos']['y'] + point[props['idx']['y']] * props['sgn']['y']
            z = props['pos']['z'] + point[props['idx']['z']] * props['sgn']['z']
            normalized = [x, y, z]
            if not normalized in points_normalized:
                points_normalized.append(normalized)
for point in sorted(points_normalized):
    print(point)
print(f'Result: {len(points_normalized)}')
