/*
 *
 *  Copyright (c) 2013, The Linux Foundation. All rights reserved.
 *  Not a Contribution, Apache license notifications and license are retained
 *  for attribution purposes only.
 *
 * Copyright (C) 2012 The Android Open Source Project
 * Copyright (C) 2021 The LineageOS Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef _BDROID_BUILDCFG_H
#define _BDROID_BUILDCFG_H

#pragma push_macro("PROPERTY_VALUE_MAX")

#if !defined(OS_GENERIC)
#include <cutils/properties.h>
#include <string.h>

static inline const char* getBTDefaultName()
{
    char device[PROPERTY_VALUE_MAX];
    property_get("ro.bootloader", device, "");

    if (strstr(device, "A525") != NULL) {
        return "Galaxy A52 4G";
    }

    if (strstr(device, "A725") != NULL) {
        return "Galaxy A72";
    }

    return "Samsung Galaxy A52/A72 4G";
}

#define BTM_DEF_LOCAL_NAME getBTDefaultName()
#endif /* OS_GENERIC */

#define BLE_VND_INCLUDED   TRUE
#define MAX_ACL_CONNECTIONS   16
#define MAX_L2CAP_CHANNELS    32
#define GATT_MAX_PHY_CHANNEL  10

#define AVDT_NUM_SEPS 35

#pragma pop_macro("PROPERTY_VALUE_MAX")

#endif
