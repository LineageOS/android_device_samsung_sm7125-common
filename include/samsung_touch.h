/*
 * SPDX-FileCopyrightText: 2021-2025 The LineageOS Project
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

/*
 * Board specific nodes
 *
 * If your kernel exposes these controls in another place, you can either
 * symlink to the locations given here, or override this header in your
 * device tree.
 */

// For GloveMode
#define TSP_CMD_LIST_NODE "/sys/class/sec/tsp/cmd_list"
#define TSP_CMD_RESULT_NODE "/sys/class/sec/tsp/cmd_result"
#define TSP_CMD_NODE "/sys/class/sec/tsp/cmd"
