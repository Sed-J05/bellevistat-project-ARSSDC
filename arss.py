import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math

def plot_habitabilityDashboard():
    #Generates an advanced multi-panel dashboard mapping out the habitability parameter space.
    radii_array = np.linspace(50, 1000, 500)
    rpms_array = np.linspace(0.5, 6, 500)
    r_gridMap, w_gridMap = np.meshgrid(radii_array, rpms_array)

    # Physics Calculations
    omega_radGrid = w_gridMap * (np.pi / 30)
    gForce_grid = (omega_radGrid**2 * r_gridMap) / 9.81
    gradient_array = (2 / radii_array) * 100

    # Configure Visualization Space
    plt.style.use('dark_background')
    fig_main = plt.figure(figsize=(14, 9))
    fig_main.suptitle('Bellevistat Artificial Gravity & Habitability Analysis', fontsize=18, fontweight='bold', y=0.96)
    gs_layout = gridspec.GridSpec(2, 2, height_ratios=[2, 1], hspace=0.3, wspace=0.2)

    # Top Panel: Contour Map
    ax_contourMap = fig_main.add_subplot(gs_layout[0, :])
    contour_plot = ax_contourMap.contourf(r_gridMap, w_gridMap, gForce_grid, levels=np.linspace(0, 2, 21), cmap='inferno', alpha=0.8)
    cbar_main = fig_main.colorbar(contour_plot, ax=ax_contourMap)
    cbar_main.set_label('Simulated Gravity (G)', rotation=270, labelpad=15)

    cg_linePlot = ax_contourMap.contour(r_gridMap, w_gridMap, gForce_grid, levels=[1.0], colors='cyan', linewidths=2.5)
    ax_contourMap.clabel(cg_linePlot, inline=True, fontsize=12, fmt='1.0 G Curve')

    ax_contourMap.axhline(y=4, color='red', linestyle='--', linewidth=1.5, label='NASA Max RPM (Coriolis Limit)')
    comfort_regionMask = (gForce_grid >= 0.9) & (gForce_grid <= 1.1) & (w_gridMap <= 4.0)
    ax_contourMap.contourf(r_gridMap, w_gridMap, comfort_regionMask, levels=[0.5, 1], colors=['green'], alpha=0.3)

    ax_contourMap.set_title('Gravity Parameter Space: Radius vs. Angular Velocity', fontsize=14)
    ax_contourMap.set_xlabel('Station Radius (meters)')
    ax_contourMap.set_ylabel('Rotation Rate (RPM)')
    ax_contourMap.legend(loc='upper right')

    # Bottom Left Panel: Tangential Velocity
    ax_velocityPlot = fig_main.add_subplot(gs_layout[1, 0])
    omega_1gArray = np.sqrt(9.81 / radii_array)
    v_1gArray = omega_1gArray * radii_array

    ax_velocityPlot.plot(radii_array, v_1gArray, color='cyan', linewidth=2)
    ax_velocityPlot.fill_between(radii_array, v_1gArray, color='cyan', alpha=0.1)
    ax_velocityPlot.set_title('Tangential Velocity at 1G', fontsize=12)
    ax_velocityPlot.set_xlabel('Station Radius (meters)')
    ax_velocityPlot.set_ylabel('Velocity (m/s)')
    ax_velocityPlot.grid(color='gray', linestyle=':', alpha=0.5)

    # Bottom Right Panel: Gravity Gradient
    ax_gradientPlot = fig_main.add_subplot(gs_layout[1, 1])
    ax_gradientPlot.plot(radii_array, gradient_array, color='magenta', linewidth=2)
    ax_gradientPlot.axhline(y=15, color='red', linestyle='--', linewidth=1.5, label='Max Allowable (15%)')

    ax_gradientPlot.fill_between(radii_array, gradient_array, 15, where=(gradient_array <= 15), color='green', alpha=0.2)
    ax_gradientPlot.fill_between(radii_array, gradient_array, 15, where=(gradient_array > 15), color='red', alpha=0.2)

    ax_gradientPlot.set_title('Physiological Gravity Gradient (2m Tall Subject)', fontsize=12)
    ax_gradientPlot.set_xlabel('Station Radius (meters)')
    ax_gradientPlot.set_ylabel('Gravity Variance (%)')
    ax_gradientPlot.set_ylim(0, 5)
    ax_gradientPlot.legend(loc='upper right')
    ax_gradientPlot.grid(color='gray', linestyle=':', alpha=0.5)

    plt.show()

def run_habitability_analysis():
    #Runs the interactive terminal calculator for the station.
    print("=== Bellevistat Station Calculator & Analysis ===")
    print("1. Input known Radius (m)")
    print("2. Input target Gravity (g)")
    
    user_menuChoice = input("Select 1 or 2: ")
    
    if user_menuChoice == '1':
        radius_inputVal = float(input("Enter Radius in meters: "))
        target_gForce = 1.0 
        
        omega_radSec = math.sqrt((target_gForce * 9.81) / radius_inputVal)
        favorable_rpmValue = omega_radSec * (30 / math.pi)
        tangential_vel_ms = omega_radSec * radius_inputVal
        
        print("\n--- Results ---")
        print(f"For a radius of {radius_inputVal}m, the favorable gravity is {target_gForce}G.")
        print(f"Required Rotation: {favorable_rpmValue:.2f} RPM")
        print(f"Tangential Velocity: {tangential_vel_ms:.2f} m/s")
        
        if favorable_rpmValue > 4:
            print("WARNING: RPM exceeds NASA's 4 RPM comfort limit! Risk of Coriolis motion sickness.")
            
    elif user_menuChoice == '2':
        target_gForce = float(input("Enter Target Gravity (in Gs, e.g., 1.0): "))
        favorable_rpmValue = 2.0 #A comfortable RPM value to aim for (as described by nasa), can be adjusted based on user preference or constraints.
        
        omega_radSec = favorable_rpmValue * (math.pi / 30)
        favorable_radius_m = (target_gForce * 9.81) / (omega_radSec ** 2)
        tangential_vel_ms = omega_radSec * favorable_radius_m
        
        print("\n--- Results ---")
        print(f"For a gravity of {target_gForce}G at a highly comfortable {favorable_rpmValue} RPM:")
        print(f"Required Favorable Radius: {favorable_radius_m:.2f} meters")
        print(f"Tangential Velocity: {tangential_vel_ms:.2f} m/s")
        
    else:
        print("Invalid selection. Proceeding to calculations...")
        
    print("\n--- Agricultural Needs ---")
    try:
        pop_sizeExpected = int(input("Enter the expected population size: "))
        area_perPerson_m2 = 50.0 #change this value based on the type of agriculture (hydroponic/aeroponic) and dietary needs
        total_agriArea_m2 = pop_sizeExpected * area_perPerson_m2
        
        print(f"Total Hydroponic/Aeroponic Area Required: {total_agriArea_m2:,.2f} square meters")
        print(f"(Using ~{area_perPerson_m2} square meters per capita)")
    except ValueError:
        print("Skipping agricultural calculation.")

    print("\nLoading Visualizations...")
    print("\nRendering Advanced Habitability Dashboard...")
    plot_habitabilityDashboard()

if __name__ == "__main__":
    run_habitability_analysis()