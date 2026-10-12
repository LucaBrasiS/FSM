`timescale 1ns / 1ps

module elevator_controller (
    input  wire       clk,
    input  wire       rst_n,
    input  wire [3:0] floor_req,
    input  wire       door_sensor,
    input  wire       emergency,
    
    output reg  [1:0] current_floor,
    output reg        motor_up,
    output reg        motor_down,
    output reg        door_open,
    output reg        alarm,
    output reg  [3:0] fsm_state
);

    // Durum Kodlaması
    localparam [3:0] 
        S_IDLE      = 4'b0000,
        S_MOVING_UP = 4'b0001,
        S_MOVING_DN = 4'b0010,
        S_DECEL     = 4'b0011,
        S_DOOR_OPEN = 4'b0100,
        S_DOOR_WAIT = 4'b0101,
        S_DOOR_CLOS = 4'b0110,
        S_OBSTACLE  = 4'b0111,
        S_EMERGENCY = 4'b1000;

    reg [3:0] state_q, state_d;
    reg [3:0] req_reg;
    reg [7:0] timer_cnt;

    localparam TIMER_MOVE_LIMIT = 8'd3;
    localparam TIMER_DOOR_LIMIT = 8'd3;

    always @(*) begin
        fsm_state = state_q;
    end

    // Sıralı Mantık
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            state_q       <= S_IDLE;
            current_floor <= 2'd0;
            req_reg       <= 4'd0;
            timer_cnt     <= 8'd0;
        end else begin
            state_q <= state_d;
            req_reg <= (req_reg | floor_req);

            if (state_q == S_DOOR_OPEN) begin
                req_reg[current_floor] <= 1'b0;
            end

            if (state_q != state_d) begin
                timer_cnt <= 8'd0;
            end else begin
                timer_cnt <= timer_cnt + 1'b1;
            end

            if (state_q == S_MOVING_UP && timer_cnt + 1'b1 >= TIMER_MOVE_LIMIT) begin
                current_floor <= current_floor + 1'b1;
            end else if (state_q == S_MOVING_DN && timer_cnt + 1'b1 >= TIMER_MOVE_LIMIT) begin
                current_floor <= current_floor - 1'b1;
            end
        end
    end

    // Kombinasyonel Gelecek Durum Mantığı
    always @(*) begin
        state_d = state_q;

        if (emergency) begin
            state_d = S_EMERGENCY;
        end else begin
            case (state_q)
                S_IDLE: begin
                    if (req_reg[current_floor]) begin
                        state_d = S_DECEL;
                    end else if ((req_reg[3] && current_floor < 3) || 
                                 (req_reg[2] && current_floor < 2) || 
                                 (req_reg[1] && current_floor < 1)) begin
                        state_d = S_MOVING_UP;
                    end else if ((req_reg[0] && current_floor > 0) || 
                                 (req_reg[1] && current_floor > 1) || 
                                 (req_reg[2] && current_floor > 2)) begin
                        state_d = S_MOVING_DN;
                    end
                end

                S_MOVING_UP: begin
                    if (timer_cnt + 1'b1 >= TIMER_MOVE_LIMIT) begin
                        if (req_reg[current_floor + 1'b1] || (!req_reg[3] && !req_reg[2] && !req_reg[1] && !req_reg[0])) 
                            state_d = S_DECEL;
                        else 
                            state_d = S_MOVING_UP;
                    end
                end

                S_MOVING_DN: begin
                    if (timer_cnt + 1'b1 >= TIMER_MOVE_LIMIT) begin
                        if (req_reg[current_floor - 1'b1]) 
                            state_d = S_DECEL;
                        else 
                            state_d = S_MOVING_DN;
                    end
                end

                S_DECEL: begin
                    if (timer_cnt + 1'b1 >= 2) 
                        state_d = req_reg[current_floor] ? S_DOOR_OPEN : S_IDLE;
                end

                S_DOOR_OPEN: begin
                    if (timer_cnt + 1'b1 >= 2) 
                        state_d = S_DOOR_WAIT;
                end

                S_DOOR_WAIT: begin
                    if (timer_cnt + 1'b1 >= TIMER_DOOR_LIMIT) 
                        state_d = S_DOOR_CLOS;
                end

                S_DOOR_CLOS: begin
                    if (door_sensor) 
                        state_d = S_OBSTACLE;
                    else if (timer_cnt + 1'b1 >= 2) 
                        state_d = S_IDLE;
                end

                S_OBSTACLE: begin
                    if (timer_cnt + 1'b1 >= 2) 
                        state_d = S_DOOR_OPEN;
                end

                S_EMERGENCY: begin
                    if (!emergency) 
                        state_d = S_IDLE;
                end

                default: state_d = S_IDLE;
            endcase
        end
    end

    // Çıkış Mantığı
    always @(*) begin
        motor_up   = 1'b0;
        motor_down = 1'b0;
        door_open  = 1'b0;
        alarm      = 1'b0;

        case (state_q)
            S_MOVING_UP: motor_up = 1'b1;
            S_MOVING_DN: motor_down = 1'b1;
            S_DOOR_OPEN, S_DOOR_WAIT, S_OBSTACLE: door_open = 1'b1;
            S_EMERGENCY: alarm = 1'b1;
            default: ;
        endcase
    end

endmodule