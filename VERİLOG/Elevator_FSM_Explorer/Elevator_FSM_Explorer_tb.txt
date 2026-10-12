`timescale 1ns / 1ps

module elevator_controller_tb;

    reg       clk;
    reg       rst_n;
    reg [3:0] floor_req;
    reg       door_sensor;
    reg       emergency;
    
    wire [1:0] current_floor;
    wire       motor_up;
    wire       motor_down;
    wire       door_open;
    wire       alarm;
    wire [3:0] fsm_state;

    // Test edilecek modül (DUT)
    elevator_controller uut (
        .clk(clk),
        .rst_n(rst_n),
        .floor_req(floor_req),
        .door_sensor(door_sensor),
        .emergency(emergency),
        .current_floor(current_floor),
        .motor_up(motor_up),
        .motor_down(motor_down),
        .door_open(door_open),
        .alarm(alarm),
        .fsm_state(fsm_state)
    );

    always #5 clk = ~clk;

    initial begin
        clk         = 1'b0;
        rst_n       = 1'b0;
        floor_req   = 4'b0000;
        door_sensor = 1'b0;
        emergency   = 1'b0;

        #25;
        rst_n = 1'b1;

        // Kat 2 çağrısı gönder
        #20;
        floor_req = 4'b0100;
        #20;
        floor_req = 4'b0000;

        #400;
        $finish;
    end

    initial begin
        $monitor("Zaman = %0t ns | State = %d | Kat = %d | Motor_Up = %b | Motor_Dn = %b | Door_Open = %b", 
                 $time, fsm_state, current_floor, motor_up, motor_down, door_open);
    end

endmodule