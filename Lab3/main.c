/**************************************************************
 * main.c
 * rev 1.0 09-Aug-2022 sammo
 * Lab3
 * ***********************************************************/

#include "pico/stdlib.h"
#include <string.h>
#include <stdbool.h>
#define CONTENT_OF(addr) (*(volatile uint32_t*)addr)
typedef unsigned long uint32_t; 

#define LED_PIN 25
#define REG_GPIO25_OE (0x4001c000+0x068)

#define REG_GPIO_CTRL (0x40014000+0x0cc)

#define REG_GPIO_OE_SET (0xd0000000+0x024)
#define GPIO_OUT_SET (0xd0000000+0x014)
#define GPIO_OUT_CLR (0xd0000000+0x018)





;int main(void) {
 
 // 1. enable the pads
CONTENT_OF(REG_GPIO25_OE) = CONTENT_OF(REG_GPIO25_OE) & ((1<<6) | ~(1<<7));

// 2. select the GPIO function
CONTENT_OF(REG_GPIO_CTRL) = 5;

// 3. set the data direction
CONTENT_OF(REG_GPIO_OE_SET) = (1<<LED_PIN); 



  while (true) {
    // TODO - Repeated code here


CONTENT_OF(GPIO_OUT_SET) = (1<<LED_PIN);

for (uint32_t i = 0; i < 8000000; i++){
   __asm volatile ("nop");
   }


CONTENT_OF(GPIO_OUT_CLR) = (1<<LED_PIN);

for (uint32_t i = 0; i < 8000000; i++){
   __asm volatile ("nop");
   }
}
}