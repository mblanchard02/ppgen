/**************************************************************
 * main.c
 * rev 1.0 19-Aug-2022 blanc
 * Lab4
 * ***********************************************************/

#include "pico/stdlib.h"
#include <stdbool.h>
#include <stdio.h>

#define RED_LED 15
#define GREEN_LED 16
#define BLUE_LED 17

int main(void) {
  // TODO - Initialise components and variables
  stdio_init_all();
  printf("EG1002 Lab4 Test\r\n");
  while (true) {
    printf("Hello Matt. Good stuff\r\n");
    sleep_ms(1000);
    // TODO - Repeated code here
    // get a character using getchar_timeout_us
    //Write an if statement or a switch case to see what the character is
    // depending on the char set some GPIO pins to toggle LEDs
  }
}
