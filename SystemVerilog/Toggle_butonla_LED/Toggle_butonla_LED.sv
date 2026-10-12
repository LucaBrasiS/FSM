`timescale 1ns / 1ps

module Toggle_butonla_LED #(
    parameter HALF_PERIOD = 50_000_000
)(
    input wire clk,
    input wire rst,
    output reg led                    
);

    // Verilog'da $clog2 fonksiyonu ile dinamik bit genişliği hesaplama
    reg [$clog2(HALF_PERIOD)-1:0] cnt;
    
    always @(posedge clk) begin
        if (rst) begin
            cnt <= 0;
            led <= 1'b0;
        end 
        else if (cnt == HALF_PERIOD - 1) begin
            cnt <= 0;
            led <= ~led;
        end 
        else begin
            cnt <= cnt + 1'b1;
        end
    end
    
endmodule